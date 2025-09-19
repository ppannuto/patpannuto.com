{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    virtualenv
    pandoc
    texliveFull  # Includes all LaTeX packages including biblatex
    imagemagick
    gnumake
    git
  ];

  shellHook = ''
    echo "Setting up development environment..."
    
    # Create and activate virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
      echo "Creating Python virtual environment..."
      python3 -m venv venv
    fi
    
    source venv/bin/activate
    
    # Install Python dependencies
    if [ -f "requirements.txt" ]; then
      echo "Installing Python dependencies..."
      pip install -r requirements.txt
    fi
    
    echo "Development environment ready!"
  '';
}