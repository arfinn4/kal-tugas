import os
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset")

IMAGE_SIZE = (100, 100)


faces = []
labels = []

print("Loading dataset...")

if not os.path.exists(DATASET_PATH):
    print("Folder dataset tidak ditemukan!")
    print("Pastikan folder dataset berada di folder yang sama dengan file .py")
    exit()

for person_name in os.listdir(DATASET_PATH):

    person_folder = os.path.join(DATASET_PATH, person_name)

    if os.path.isdir(person_folder):

        for filename in os.listdir(person_folder):

            img_path = os.path.join(person_folder, filename)

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                print(f"Gagal membaca gambar: {img_path}")
                continue

            img = cv2.resize(img, IMAGE_SIZE)

            img = img / 255.0

            img_vector = img.flatten()

            faces.append(img_vector)
            labels.append(person_name)

faces = np.array(faces)
labels = np.array(labels)

if len(faces) < 2:
    print("Dataset terlalu sedikit!")
    print("Minimal membutuhkan 2 gambar")
    exit()

print("Jumlah data training :", len(faces))
print("Dimensi wajah        :", faces.shape)

print("\nMembentuk eigenspace...")

N_COMPONENTS = min(len(faces) - 1, 20)

print("Jumlah PCA components :", N_COMPONENTS)

pca = PCA(
    n_components=N_COMPONENTS,
    whiten=True,
    svd_solver='randomized'
)

training_projection = pca.fit_transform(faces)

print("Eigenspace berhasil dibuat")

test_image_path = input("\nMasukkan path gambar test: ")

test_img = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

if test_img is None:
    print("Gambar test tidak ditemukan!")
    exit()

test_img = cv2.resize(test_img, IMAGE_SIZE)

test_img_normalized = test_img / 255.0

test_vector = test_img_normalized.flatten()


test_projection = pca.transform([test_vector])

distances = euclidean_distances(
    test_projection,
    training_projection
)

closest_index = np.argmin(distances)

recognized_name = labels[closest_index]
minimum_distance = distances[0][closest_index]

THRESHOLD = 10

print("\n===== HASIL FACE RECOGNITION =====")

if minimum_distance > THRESHOLD:

    print("Wajah tidak dikenali")
    print("Distance :", minimum_distance)

else:

    print("Orang paling mirip :", recognized_name)
    print("Distance            :", minimum_distance)

matched_face = faces[closest_index].reshape(IMAGE_SIZE)

plt.figure(figsize=(8,4))

# gambar input
plt.subplot(1,2,1)
plt.imshow(test_img, cmap='gray')
plt.title("Input Wajah")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(matched_face, cmap='gray')
plt.title(f"Mirip dengan:\n{recognized_name}")
plt.axis('off')

plt.tight_layout()
plt.show()