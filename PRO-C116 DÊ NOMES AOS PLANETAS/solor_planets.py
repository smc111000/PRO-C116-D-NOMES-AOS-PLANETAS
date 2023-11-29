import cv2


img = cv2.imread("solar-system.jpg")


cv2.imshow("resultado", img)



# Exemplo para o planeta 'Mercúrio'
cv2.putText(img, "Mercúrio", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Exemplo para o planeta 'Vênus'
cv2.putText(img, "Vênus", (180, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Exemplo para o planeta 'Terra'
cv2.putText(img, "Terra", (300, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Exemplo para o planeta 'Marte'
cv2.putText(img, "Marte", (400, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

# Use cv2.waitKey(0).
cv2.waitKey(0)


cv2.imwrite("solar_systemwithname.jpg", img)
