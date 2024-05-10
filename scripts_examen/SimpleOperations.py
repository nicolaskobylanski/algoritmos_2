import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price - (price * discount)

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price + (price * tax_rate)

def main():
    # Crear una instancia de SimpleOperations
    operations = SimpleOperations()

    # Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
    twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
    vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

    # Usar las funciones preconfiguradas.
    price = 100  # Ejemplo de precio base

    # Aplicar un descuento del 20%
    discounted_price = twenty_percent_discount(price=price)
    print(f"Precio después del descuento: {discounted_price:.2f}")

    # Aplicar un impuesto del 21%
    price_with_tax = vat_tax(price=price)
    print(f"Precio después de impuestos: {price_with_tax:.2f}")

if __name__ == "__main__":
    main()
