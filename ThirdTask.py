m = int(input("Unesite maksimalan broj znakova po liniji: "))
n = int(input("Unesite minimalnu duzinu linije: "))

print("Unesite tekst (za kraj unesite prazan redak):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

def center_text(line, m, n):
    line_length = len(line)
    if line_length >= m:
        return line[:m]  
    spaces_needed = m - line_length
    left_padding = spaces_needed // 2
    right_padding = spaces_needed - left_padding
    return ' ' * left_padding + line + ' ' * right_padding

for line in lines:
    centered_line = center_text(line, m, n)
    if len(centered_line) < n:
        centered_line = centered_line.ljust(n)
    print(centered_line)