# SQLite Tutorial

## Link to [Website with Tutorial](https://www.sqlitetutorial.net)

## Description
Will update description after learning more about the project.


## Notes from SQLite Install using Homebrew
If you need to have sqlite first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"' >> ~/.zshrc

For compilers to find sqlite you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include"