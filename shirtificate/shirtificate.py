from fpdf import FPDF

def main():
    name = input("Enter your name: ")
    generate_shirtificate(name)

def generate_shirtificate(name):
    pdf = FPDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=16)
    pdf.cell(200, 10, text="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=14)
    pdf.set_xy(10, 70)
    pdf.cell(190, 70, text=name + " took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
