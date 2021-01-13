# Command-processor
A thing which you can use to register and process terminal style commands

# Usage
- Instantiate the `CommandProcessor` class
  ```python
  command_processor = CommandProcessor()
  ```
- Instantiate the `Command` class to make a command. This class takes a `name`, an optional `description` and an optional `command`:
  - The command parameter is a reference to a function that will be called when the command is executed
  - The function must take a parameter, which will be all the arguements that have been specified when a command is executed
  ```python
  def hello_world(args):
    print('hello world')
    print(args)
  
  # syntax: Command(name, description, command)
  command = Command('hello', 'prints hello world', hello_world)
  ```
- Register commands to the processor by using `.register_command()`
  ```python
  command_processor.register_command(command)
  ```
- Execute commands by using `.execute()`
  - This method takes a command as a string input, which is then processed.
  ```python
  command_processor.execute('hello foo bar')
  
  # Output
  hello world
  ['foo', 'bar']
  ```
- If the command can't be executed, the processor returns `error`
