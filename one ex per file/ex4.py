# part 4
# task: abbreviate a potentially long string s to have the x first and x last chars with ... in between
# for x = 5 this would be: "A very long description" => "A ver...ption" (... is called filler)
# in a loop, set x from 5 to and to 15 and print out x and the abbreviated version 
# there'll be an issue where the result would actually be longer(!) than the un-abbreviated s. 
# For these cases, do not perform your abbreviation, simply print out s. Note that this
# should work for any other string a or filler as well, so don't hardcode things!
# 
# Optional:
# write a general function abbr(s, filler="...", total_width=15) which abbreviates s
# to total_width chars and uses the string filler in between them. Again, make sure the
# result would not be longer than s!
# call your function a couple of times with different parameters and also test edge cases
print("start of part 4") # set breakpoint here
s = "A very long description" # a long string
filler = "..."
for num in range(5, 15):
    # validate that abbreviated isn't too long
    if num * 2 + len(filler) > len(s):
        print(num, s)
    else:
        abbreviated = s[0:num] + filler + s[-num:]
        print(num, abbreviated)
   
print("end of 4") # set breakpoint here 
