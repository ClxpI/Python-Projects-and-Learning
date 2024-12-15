firstname = 'World'
o2 = 21
hi= "Hi! I'm " + firstname + ".My atmosphere is" + str(o2) + "% oxygen." #text without correct spacing
print(hi)

hi = "Hi! I'm {}. My atmosphere is {}% oxygen.".format(firstname, o2) #text with correct spacing
print(hi)
