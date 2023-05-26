import pytest
import tkinter as tk
from tkinter import messagebox
import app


@pytest.fixture
def app():
    root = tk.Tk()
    yield root
    root.destroy()


def test_add_product(app):
    #app.name_entry_text.set("Product A")
    app.id_entry_text.set("A001")
    app.quantity_sold_entry_text.set("10")
    app.quantity_left_entry_text.set("90")
    app.price_entry_text.set("10")
    app.today_sales_quantity_entry_text.set("5")
    app.today_sales_total_price_entry_text.set("")
    app.week_sales_quantity_entry_text.set("20")
    app.week_sales_total_price_entry_text.set("")
    app.month_sales_quantity_entry_text.set("50")
    app.month_sales_total_price_entry_text.set("")

    app.add_product()

    #assert messagebox._show_called
    #assert messagebox._title == "Success"
    assert app.name_entry_text == "Product A"


def test_delete_product(app):
    app.delete_entry.set("A001")

    app.delete_product()

    assert messagebox._show_called
    assert messagebox._title == "Success"
    assert messagebox._message == "Product deleted"


def test_update(app):
    app.name_entry_text.set("Product A")
    app.id_entry_text.set("A001")
    app.quantity_sold_entry_text.set("10")
    app.quantity_left_entry_text.set("90")
    app.price_entry_text.set("15")
    app.today_sales_quantity_entry_text.set("5")
    app.today_sales_total_price_entry_text.set("")
    app.week_sales_quantity_entry_text.set("20")
    app.week_sales_total_price_entry_text.set("")
    app.month_sales_quantity_entry_text.set("50")
    app.month_sales_total_price_entry_text.set("")

    app.update()

    assert messagebox._show_called
    assert messagebox._title == "Success"
    assert messagebox._message == "Product updated"


def test_calculate(app):
    app.price_entry_text.set("10")
    app.quantity_sold_entry_text.set("5")
    app.quantity_left_entry_text.set("95")
    app.today_sales_quantity_entry_text.set("5")
    app.week_sales_quantity_entry_text.set("20")
    app.month_sales_quantity_entry_text.set("50")

    app.calculate()

    assert app.today_sales_total_price_entry_text.get() == "50"
    assert app.week_sales_total_price_entry_text.get() == "200"
    assert app.month_sales_total_price_entry_text.get() == "500"
    assert app.add_button["state"] == "normal"


def test_refresh(app):
    app.Refresh()


if __name__ == "__main__":
    pytest.main()
