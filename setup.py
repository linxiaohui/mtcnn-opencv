import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mtcnn-opencv",
    version="1.0.2",
    author="linxiaohui",
    author_email="llinxiaohui@126.com",
    description="MTCNN face detection using OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linxiaohui/mtcnn-opencv",
    packages=setuptools.find_packages(),
    package_data={
        'mtcnn_cv2': ['pnet.onnx', 'rnet.onnx', 'onet.onnx']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires='>=3.6',
)
