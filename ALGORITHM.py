# ADG ID PROJECT
# Apache License
# 2024 Aimar, Guillermo, Daniel, Ancor

def order_dni(dni_list):
    def order_key(dni):
        number = int(dni[:-1])
        letter = dni[-1]        
        return (letter, number)
    ordered_list = sorted(dni_list, key=order_key)
    return ordered_list

dni_list = ["12345678A", "87654321B", "23456789A", "34567890C", "12345678B","68753098X", "49496892G","27569049P","101C" ]
ordered_dni = order_dni(dni_list)
print("ordered list:", ordered_dni)
