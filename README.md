# QR Code Generator

A simple Python application that generates a QR code from a URL and saves it as an image file. The generated QR code can be viewed immediately after creation.

## Features

* Generate QR codes from URLs or text
* Save QR codes as PNG images
* Automatically open the generated QR code
* Easy to customize for other QR code formats such as SMS, email, and contact information

## Technologies Used

* Python 3
* qrcode

## Project Structure

```text
qr-code-generator/
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Matin-python/Create-QRCode.git
cd qr-code-generator
```

### 2. Install dependencies

```bash
pip install qrcode[pil]
```

## Usage

Edit the `data` variable in `main.py`:

```python
data = "https://github.com/Matin-python/"
```

Run the application:

```bash
python main.py
```

The program will:

1. Generate a QR code from the provided data.
2. Save it as:

```text
QR Code Output.png
```

3. Open the generated image automatically.

## Example

### URL QR Code

```python
data = "https://github.com/Matin-python/"
```

### SMS QR Code

```python
data = "SMSTO:+989123456789:Hi, How are you doing?"
```

## Future Improvements

* Accept user input from the terminal
* Support custom file names
* Add QR code color customization
* Add logo insertion inside QR codes
* Create a graphical user interface (GUI)
* Generate QR codes for Wi-Fi credentials and contact cards

## License

This project is licensed under the MIT License.

## Author

**Mohammad Reza Bakhshandeh**

Electrical Engineering (Electronics) Graduate

Interested in Python Development, Computer Vision, Machine Learning, and Artificial Intelligence.
