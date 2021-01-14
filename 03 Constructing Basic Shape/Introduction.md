### Construction Basic Shapes in OpenCV

When building a computer vision project, you usually want to modify the image by drawing some shapes. For example, if you develop a face detection algorithm, you should draw a rectangle highlighting the detected faces in the computed image.       
      
The following topics will be covered in this module:
1. A theoretical introduction to drawing in OpenCV
2. Basic shapes—lines, rectangles, and circles
3. Basic shapes (2)—clip and arrowed lines, ellipses, and polylines
4. Drawing text
5. Dynamic drawing with mouse events
6. Advanced drawing

BASIC TERMINOLGOIES
1. img: the image where the shape will be drawn
2. color: color (BGR triplet) used to draw the shape
3. thickness: if positive shape outline will be drawn
              if negative filled shape will be  drawn
4. lineType: type of the shape boundary
 OpenCV provides three types of shape boundary
   cv2.LINE_4 - 4 connected lines
   cv2.LINE_8 - 8 connected lines
   cv2.LINE_AA - anti-aliased lines
5. shift: number of fractional bits in connection with coordinates of some points defining the shape

