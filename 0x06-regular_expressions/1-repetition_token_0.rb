#!/usr/bin/env ruby
# A Ruby script that check if the argument matches the regular expression
# for "School" (case-sensitive).

def match_str(input)
  regex = /hbt{2,5}n/
  return input.match(regex)
end

# To get argument from command-line
input_arg = ARGV[0]

if input_arg
  matched_string = match_str(input_arg)
  if matched_string
    puts matched_string
  else
    puts ""
  end
else
  puts "User: ./1-repetition_token_0.rb argument"
end
