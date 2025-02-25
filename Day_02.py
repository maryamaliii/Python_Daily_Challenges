# Daily Python Challenge Day_02

Teachers="SirAmeen , SirDaniyal , SirHamzaSyed , SirAliJawwad , SirMubashir , SirAsharib "
Teacher=Teachers.split (",")
print(Teacher)
#output
#['SirAmeen ', ' SirDaniyal ', ' SirHamzaSyed ', ' SirAliJawwad ', ' SirMubashir ', ' SirAsharib ']

print(len(Teacher))
#output
#6

Teacher.reverse()
print(Teacher)
#output 
#[' SirAsharib ', ' SirMubashir ', ' SirAliJawwad ', ' SirHamzaSyed ', ' SirDaniyal ', 'SirAmeen ']

fvrt_Teachers= " ".join(Teacher)
print(fvrt_Teachers)
#output 
#SirAsharib  SirMubashir  SirAliJawwad  SirHamzaSyed  SirDaniyal SirAmeen



