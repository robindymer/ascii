#include<opencv2/opencv.hpp>
#include<iostream>

// Nullify the need of cv::function()
using namespace std;
using namespace cv;

// Read img
Mat img_grayscale = imread("test.jpg", 0);

// Display img
imgshow("grayscale image", img_grayscale);

// Wait for keystroke
waitKey(0);

// Destroy all the windows created
destroyAllWindows();

imwrite("grayscsale.jpg", img_grayscale);
