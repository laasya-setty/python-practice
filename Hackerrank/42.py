# find angle MBC
import math
ab=int(input())
bc=int(input())
ca=math.hypot(ab,bc)
h=ca/2
bc=bc/2
Output = int(round(math.degrees(math.acos(bc/h))))

Output = str(Output)

print(Output+u"\N{DEGREE SIGN}")
