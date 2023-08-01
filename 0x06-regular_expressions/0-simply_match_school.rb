#!/usr/bin/env ruby
# A Ruby script that check if the argument matches the regular expression
# for "School" (case-sensitive).

def match_school(input)
  regex = /School/ # Removed the "i" flag to make the regex case-sensitive
  return input.scan(regex).flatten
end

# To get argument from command-line
input_arg = ARGV[0]

if input_arg
  matched_strings = match_school(input_arg)
  if matched_strings.any?
    puts matched_strings.join
  else
    puts ""
  end
else
  puts "User: ./0-simply_match_school.rb argument"
end
