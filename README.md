# Document Scanner with OpenCV

This is a Python-based Document Scanner that utilizes the OpenCV library to capture, preprocess, and transform an image of a document into a scanned perspective. The application works with your webcam to detect the edges of the document, apply perspective transformation, and produce a scanned output of the document.

## How it Works

1. The program uses OpenCV to capture frames from your webcam with a resolution of 640x480 pixels.

2. Preprocessing steps are applied to the captured frame to enhance the document's edges. These steps include converting the frame to grayscale, applying Gaussian blurring to reduce noise, and detecting edges using the Canny edge detection algorithm.

3. The program then identifies the largest contour in the frame, which represents the outline of the document. The contour is approximated to a quadrilateral shape using the Ramer–Douglas–Peucker algorithm.

4. The program reorders the points of the quadrilateral to correct any orientation issues.

5. Using the reordered points, the perspective transformation matrix is calculated using `cv2.getPerspectiveTransform()` to obtain a bird's-eye view of the document.

6. The image is warped according to the transformation matrix to create the final scanned output.

## Setup and Usage

To use the Document Scanner, make sure you have Python and the required libraries installed. You can run the script, and the webcam will open, displaying the original frame, the contour with the detected document, and the final scanned output.

To terminate the application, press the 'q' key.

## Requirements

- Python 3.x
- OpenCV

## How to Run

1. Ensure you have Python and OpenCV installed on your system.

2. Clone or download the project repository to your local machine.

3. Navigate to the project directory and execute the script using the following command:

```python document_scanner.py```


4. The webcam will open, and you can position a document within the camera's view.

5. When you're ready, press the 'q' key to terminate the application and exit.

<!-- ## Example Output

![Document Scanner Output](example_output.jpg) -->

## Credits

This project was created by [YourName]. It is inspired by various computer vision techniques and the power of OpenCV.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

