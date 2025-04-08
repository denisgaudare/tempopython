import unicodedata

lettre = "e"
accent = "éàèèèèAbbèè"  # Lettre "é" en un seul caractère
nfd_text = unicodedata.normalize("NFD", accent)
without_accents = ''.join(c for c in nfd_text if unicodedata.category(c) != 'Mn')

lc = unicodedata.category(lettre)
print(lc)
ac = unicodedata.category(accent)
print(ac)
for c in nfd_text:
    print(f"[{c}]", unicodedata.category(c))

print(lc,ac)


# Remove accen