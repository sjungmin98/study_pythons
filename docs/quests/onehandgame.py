space_first="1"
space_second=""
space_third="2"
space_fourth=""
space_fifth="3"

print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))
space_fourth=space_third
space_third=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))

space_third=space_fifth
space_fifth=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))

space_second=space_first
space_first=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))

space_first=space_third
space_third=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))

space_third=space_fourth
space_fourth=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))

space_fifth=space_second
space_second=""
print("{}/{}/{}/{}/{}" .format(space_first, space_second, space_third, space_fourth, space_fifth))



