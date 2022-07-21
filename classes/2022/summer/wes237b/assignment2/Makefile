# Convention, `all` is a phony target that builds everything
# and must be listed first
.PHONY: all
all:	$(BIN)

###
# Setup & config
###

BUILD_DIR := build/

# What binary are we trying to build?
BIN := vectest

# C++ source files
CXXSRCS := $(wildcard src/*.cxx)

# Create list of objects to build
OBJS := $(CXXSRCS:%.cxx=$(BUILD_DIR)/%.o)

# Any flags for the C++ compiler?
CXXFLAGS += -Iinclude

# Libraries
LDFLAGS += -llapack -lblas -larmadillo

###
# Build rules
###

# Binary depends on its objects (use default build rules)
$(BIN): $(OBJS)

###
# Convenience targets
###

.PHONY: clean
clean:
	rm -rf build/*
	rm -f $(BIN)
