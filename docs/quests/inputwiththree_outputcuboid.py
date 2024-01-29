# * quest
# - 가로 * 세로 * 높이
# - input : 가로 세로 높이
# - output : 가로()m * 세로()m * 높이()m = 직육면체()m^3 

str_input=input("가로 세로 높이 : ")
str_output_fir, str_output_sec, str_output_thi= (str_input.split())
num_output_fir=int(str_output_fir)
num_output_sec=int(str_output_sec)
num_output_thi=int(str_output_thi)
num_output_cuboid=num_output_fir* num_output_sec* num_output_thi
output=input("가로({})m * 세로({})m * 높이({})m = 직육면체 ({})m^3". format(num_output_fir, num_output_sec, num_output_thi, num_output_cuboid))

pass 