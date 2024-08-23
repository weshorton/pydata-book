# myScript.py
# import myModule and do stuff with it

### Remember that there are multiple ways to import modules

# 1. only import specific stuff:
# from myModule import g, PI

# 2. import the whole module:
# import myModule

# 3. Rename stuff during import with `as`:
import myModule as mm
from myModule import PI as pi, g as gf

# Execute some stuff with the module
print(pi)

result1 = mm.f(pi) # have to call mm here b/c didn't import it
print(result1)

result2 = gf(5, pi) # don't need mm here because imported g/gf explicitly
print(result2)

print(mm.PI) # even though I imported PI as pi, I can still use mm.PI
