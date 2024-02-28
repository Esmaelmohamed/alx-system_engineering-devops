# Check if the argument matches the regular expression
def match_school(argument)
  if argument.match(/School/)
    puts "The argument contains 'School'."
  else
    puts "The argument does not contain 'School'."
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide an argument."
else
  # Get the first argument passed from the command line
  argument = ARGV[0]
  # Call the method to match the regular expression
  match_school(argument)
end

