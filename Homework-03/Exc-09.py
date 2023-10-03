def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    print(cost_delivery.__doc__)
    return result


print(cost_delivery(2, 1, 2, 3, discount=0.5))
