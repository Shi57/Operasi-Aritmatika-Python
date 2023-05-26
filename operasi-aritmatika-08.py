a = 7
b = 2

# operasi perjumlahan +
hasil = a + b
print(a, ("+"), b ,("="), hasil)

# operasi pengurangan -
hasil = a - b
print(a, ("-"), b ,("="), hasil)

# operasi perkalian *
hasil = a * b
print(a, ("*"), b ,("="), hasil)

# operasi pembagian /
hasil = a / b
print(a, ("/"), b ,("="), hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, ("**"), b ,("="), hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print(a, ("%"), b ,("="), hasil)

# operasi floor division // (hasil pembagian yang dibulatkan)
hasil = a // b
print(a, ("//"), b ,("="), hasil)



# prioritas operasi, operational precedence
'''
  1. ()
  2. eksponen **
  3. perkalian dan teman teman * / ** //
  4. pertambahan dan pengurangan 
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y ,'*' ,z ,'+' ,x ,'/', y, '-', y ,'%' ,z ,'//', x, '=', hasil)

# kurung akan mengambil angka pertama
hasil = (x + y) * z
print('(',x, '+', y,')', '*', z, '=', hasil)