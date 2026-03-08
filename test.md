# persamaan linear
# 1. Apa yang dimaksud persaamaan linear
persamaan Linear adalah salah satu persamaan dari ilmu aljabar di mana persamaan ini sukunya mengandung konstanta dengan variabel tunggal

# 2. buat dua persamaan linear dengan dua variable
![alt text](image-1.png)

# Persamaan Linier
Persamaan Linier adalah salah satu persamaan dari ilmu aljabar dimana persamaan ini sukunya mengandung konstanta dengan variabel tunggal. Mengapa disebut linier, karena hubungan matematis ini digambarkan dengan garis lurus dalam sistem koordinat kartesius

# Sifat Persamaan Linier
- Persamaan linier memiliki beberapa sifat, yaitu:
- Penjumlahan dan pengurangan bilangan kedua ruas tidak akan mengubah persamaan nilai.
- Perkalian dan pembagian bilangan kedua ruas tidak mengubah nilai persamaan.
- Nilai persamaan tidak berubah jika kedua ruas ditambah atau dikurangi bilangan yang sama.
- Suatu persamaan jika dipindah ruas maka penjumlahan berubah jadi pengurangan, perkalian berubah menjadi pembagian, dan sebaliknya

# Jenis-Jenis Persamaan Linier
## Persamaan Linier Satu Variabel
Persamaan linier satu variabel hanya mengandung satu variabel berpangkat satu yang berpentuk kalimat terbuka dengan dihubungkan tanda =.
Kalimat terbuka di sini berarti adalah kalimat yang belum tahu kebenaranya atau bisa jadi benar, bisa jadi juga salah.
Bentuk umum dari persamaan Linear Satu Variabel: 

$ax + b = 0$

keterangan:
a = koefisien
b = konstanta
x = variabel
a dan b adalah bilangan riil
a dan b bukan nol
Namun, yang perlu digaris bawahi adalah variabel tidak selalu menggunakan lambang x, bisa jadi menggunakan y atau yang lainnya

$$10x + 2 = 22 \quad x = \frac{22-2}{10} \quad x = 2$$
Maka nilai dari huruf x adalah 2


# Persamaan Linier Dua Variabel
Sesuai dengan namanya, Persamaan Linear Dua Variabel merupakan sistem persamaan dengan variabel yang berjumlah dua dengan berpangkat 1. Persamaan linear dua variabel menggunakan relasi = dan tidak ada perkalian variabel di setiap persamaan.
Bentuk umum dari Persamaan Linear Dua Variabel adalah:

$ax + by = c$

Persamaan Linear Dua Variabel bisa diselesaikan dengan dua metode, yaitu metode substitusi dan metode eliminasi.
Metode Substitusi digunakan dengan cara mengubah satu variabel dengan variabel persamaan lain. Sedangkan Metode Eliminasi dengan cara menghapus salah satu variabel dalam persamaan
Contoh sederhana:

$​2x+4y=12$
$2x+2y=8$

Berapa nilai x dan y?
Persamaan tersebut dapat diselesaikan dengan metode subtitusi. Yaitu dengan cara pertama memilih salah satu 

$2x+4y=12$

Kemudian kita pindahkan satu variabel ke ruas lainnya

$2x=12−4y$

untuk menghilangkan variabel x maka dibagi dengan nilai koefisien x

$\frac{2x}{2} = 12 - \frac{4y}{2}\$
$x = 6 - 2y$

Jadi nilai x untuk sementara adalah 6 - 2y. Kemudian untuk mencari nilai y masukan ke dalam persamaan kedua

$2x+2y=8$
$2(6−2y)+2y=$8$
$12−4y+2y=8$
$−2y=8−12$
$−2y=−4$
 
Untuk menghilangkan variabel ya maka dibagi dengan nilai koefisien y

$\begin{aligned}\frac{-2y}{-2} &= \frac{-4}{-2} \\y &= 2\end{aligned}$

Setelah nilai y ditemukan kemudian masukan ke nilai x sementara tadi 

$x=6−2y$
$x=6−2(2)$$
$x=2$$
​
# Persamaan Linier Tiga Variabel
 Persamaan linear tiga variabel merupakan bentuk perluasan dari persamaan linear dua variabel. Sama seperti persamaan linear dua variabel, persamaan ini juga bisa diselesaikan dengan dua metode, yaitu substitusi dan eliminasi

Bentuk umum persamaan linear tiga variabel adalah:

$ax+by+cz=d$
Contoh:

$x+y+z=8$
$x+2y+2z=14$
$2x+y+2z=13$

Penyelesaian:

$x+y+z=8$

Karena nilai koefisien dari x tidak ada, maka kita hanya perlu memindah dua variabel ke kanan

$z=8–x–y$

Kemudian masukan persamaan salah satu persamaan

$x+2y+2(8–x–y)=14$
$x+2y+16–2x–2y=14$
$−x+16=14$
$−x=14−16$
$−x=−2$
$x=2$

Setelah nilai x ditemukan nilai 2 masukan ke persamaan lainnya untuk menentukan y

$2x+y+2z=13$
$2(2)+y+2(8–2–y)=13$
$4+y+16–4–2y=13$
$20–4–y=13$
$16–y=13$
$−y=13−16$
$−y=−3$
$y=3$

Kemudian untuk menentukan nilai z, masukan nilai x dan y ke nilai z sementara 

$z=8–x–y$
$z=8–2–3$
$z=3$

Maka nilai x = 2, nilai y = 3, dan nilai z = 3

## 1. sistem persamaan linear
$\begin{aligned}
x + y + z + u + v &= 15 \\
2x + y + z + u + v &= 16 \\
x + 2y + z + u + v &= 16 \\
x + y + 2z + u + v &= 17 \\
x + y + z + 2u + v &= 19
\end{aligned}$

## 2. Matriks
$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
2 & 1 & 1 & 1 & 1 & 16 \\
1 & 2 & 1 & 1 & 1 & 16 \\
1 & 1 & 2 & 1 & 1 & 17 \\
1 & 1 & 1 & 2 & 1 & 19
\end{array}
\right]$

# 3. Eliminasi Gauss
## Langkah pertama
hilangkan elemen dibawah pivot kolom pertama
$$\begin{aligned}
R_2 &\rightarrow R_2 - 2R_1 \\
R_3 &\rightarrow R_3 - R_1 \\
R_4 &\rightarrow R_4 - R_1 \\
R_5 &\rightarrow R_5 - R_1
\end{aligned}$$

## Langkah Kedua
Tukar baris pivot
$R_2 \leftrightarrow R_3$
$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & -1 & -1 & -1 & -1 & -14 \\
0 & 0 & 1 & 0 & 0 & 2 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]$

## Langkah ketiga
hilangkan elemen dibawah pivot kedua
$R_3 \rightarrow R_3 + R_2$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & -1 & -1 & -1 & -13 \\
0 & 0 & 1 & 0 & 0 & 2 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]$

## Langkah keempat
hilangkan elemen kolom ketiga
$R_3 \rightarrow -R_3$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 1 & 13 \\
0 & 0 & 1 & 0 & 0 & 2 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]$

$R_4 \rightarrow R_4 - R_3$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 1 & 13 \\
0 & 0 & 0 & -1 & -1 & -11 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]$

## Langkah kelima
hilangkan elemen kolom keempat
$R_4 \rightarrow -R_4$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 1 & 13 \\
0 & 0 & 0 & 1 & 1 & 11 \\
0 & 0 & 0 & 1 & 0 & 4
\end{array}
\right]$

$R_5 \rightarrow R_5 - R_4$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 1 & 13 \\
0 & 0 & 0 & 1 & 1 & 11 \\
0 & 0 & 0 & 0 & -1 & -7
\end{array}
\right]$

## Langkah keenam
$R_5 \rightarrow -R_5$

$\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 0 & 0 & 3 \\
0 & 0 & 0 & 1 & 0 & 4 \\
0 & 0 & 0 & 0 & 1 & 5
\end{array}
\right]$

# 4. Substitusi Balik
$v=5$$$$
$u=4$
$z=3$
$y=2$
$x=1$

# 5.kode sagecell

![alt text](image-2.png)

![alt text](image-3.png)
