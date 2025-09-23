cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
print("___|___|___")
print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
print("___|___|___")
print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
print("   |   |   ")

if cells[0]==1:
    cells[0]="X"
    
print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
print("___|___|___")
print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
print("___|___|___")
print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
print("   |   |   ")