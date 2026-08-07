# Lê a linha de entrada e separa os valores
data_input = input().strip().split()

def total_order_value_with_discount (data_input):
  total_order_value = float(data_input[0])
  discount_percentage = int(data_input[1])
  discount_value = total_order_value * (discount_percentage / 100)
  final_value = total_order_value - discount_value
  return final_value

# Imprima o valor final com duas casas decimais
print(f"{total_order_value_with_discount(data_input):.2f}")