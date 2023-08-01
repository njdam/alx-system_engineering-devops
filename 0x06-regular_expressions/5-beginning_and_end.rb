#!/usr/bin/env ruby
# A Ruby script that check if the argument matches the regular expression
# for Not quite HBTN yet (case-sensitive).

puts ARGV[0].scan(/\Ah.*n\z/).join
