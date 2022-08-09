# Quick bonus cache notes

I find it easiest to think about how they are implemented.
The cache controller uses bits from the memory address to make all of its decisions — that is how you end up with stuff being tied to powers of two.

From there, it’s all about answering the question “how will the cache controller know where to find/put this data”?
An equivalent question can be, “given the design of this cache, what are all the valid places data for a given address could be found?”

So now we have an address and we have to break it down:

 1. Chop the block offset bits off the end.
    We store stuff in the cache in whole blocks of a fixed size, so we will only use block offset bits to index into a data block once we’ve found it.
    We won’t use BO bits to find a block holding data.
 2. How many blocks are there total?
    This is just a question of cache size and block size, we haven’t gotten to organization yet.
    Just how many unique blocks does this cache have to organize?
    `NUM_BLOCKS = CACHE_SIZE / BLOCK_SIZE` — easier to do this math in bits than division usually, i.e. a `32 kB` cache has `2^15` bytes, if you have `16 byte` blocks, that’s `2^4 bytes per block`, so `2^15 / 2^4 = 2^11` (keeping things in powers of two lets you subtract exponents rather than trying to do division of large numbers [[usually*](#non2)]).
 3. How is this cache organized?
    Aka, how many different blocks could the same address be stored in?
    Aka, how associative is this cache?
    A direct-mapped cache has an associativity of `1`, every address can only end up in one block;
    a fully-associative cache has an associativity of `num_blocks`, every address could end up in any block;
    most common is a small-`n` associativity, every address could end up in some `n` blocks.
    Based on the associativity, we compute the number of _sets_.
    A set is the set of blocks that could hold a given address.
    This is the only stumbling point where `n` does not need to be a power of two[*](#non2).
    Let’s say this is `8-way Set Associative`.
    Given that we have `2^11 blocks` and each set is now defined to have `8 blocks`, that means we have `2^11/2^3=2^8 sets`.
 4. Now, we want to know which set this address belongs to.
    That is what the index is for.
    The index must be able to uniquely identify a set (by definition).
    If we have `2^8 sets`, then we have `8 index bits`.
 5. Okay, so what about tags?
    Well, the core of the cache itself only stores whole blocks of data.
    So how does the cache controller know which address that data belongs to?
    That’s the purpose of the tag (.. and index, bear with me).
    The tag is made up of all the address bits that are leftover.
    How big is the tag?
    Well, so far we’ve used `4 bits for block offset` and `8 bits for index`.
    We also need to know how big memory is.
    If we have a full `64 bits of memory space`, then the `tag is 64-8-4 = 52 bits`.
    Often memory/cache controllers will limit this — most machines don’t have 16 exbibytes of RAM! — “1 TB ought to be enough for anybody,” perhaps, so it might limit addressable memory to, say, just `40 bits` (note: the _virtual address_ presented to applications will still be 64 bits, it’s just the _physical address space_ that is limited here).
    On such a machine, we would have `40-8-4 = 28 tag bits.`
 6. Why did I say “tag and index” identify a block?
    It’s because they work together.
    Direct-mapped caches have the shortest tags, because the index limits what data can go into each block.
    For the same cache size if you change to 2-way associative, you’ll have one fewer index bit (as each set is now twice as large, and so you have half as many sets).
    The cache structure now gives you less information about which address could be in each block, so the one fewer bit of index ends up as one more bit of tag.


## <a name="non2"></a> The non-power of two case

When you have associativity that’s not a power of two, then you have to do some division directly.
e.g., If you have a `384 kB cache` with `16 B blocks`, that’s `384 kB / 16 B = 24 k blocks`.

> (but it’s also `(3*2^17) / 2^4 = 3*2^13` — there will always be an integer factor you can pull out; just not always obvious at first, so sometimes you just have to do the division.)

If this machine is 3-way set associative, then those `24 k blocks` turn into `8 k sets` or `2^13 sets`, nice clean powers of two again.

# [Back](index.html)
