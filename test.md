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
$x_1 + x_2 + x_3 + x_4 + x_5 &= 15 
2x_1 + x_2 + x_3 + x_4 + x_5 &= 16 
x_1 + 2x_2 + x_3 + x_4 + x_5 &= 17 
x_1 + x_2 + 2x_3 + x_4 + x_5 &= 18 
x_1 + x_2 + x_3 + 2x_4 + x_5 &= 19$

## Matrik
$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
2&1&1&1&1&16\\
1&2&1&1&1&17\\
1&1&2&1&1&18\\
1&1&1&2&1&19
\end{array}
\right]$

## Langkah pertama
$R_2 \rightarrow R_2 - 2R_1$ \\
$R_3 \rightarrow R_3 - R_1$ \\
$R_4 \rightarrow R_4 - R_1$ \\
$R_5 \rightarrow R_5 - R_1$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&-1&-1&-1&-1&-14\\
0&1&0&0&0&2\\
0&0&1&0&0&3\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah kedua

$R_2 \rightarrow -R_2$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&1&0&0&0&2\\
0&0&1&0&0&3\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah ketiga

$R_3 \rightarrow R_3 - R_2$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&-1&-1&-1&-12\\
0&0&1&0&0&3\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah keempat

$R_3 \rightarrow -R_3$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&1&1&1&12\\
0&0&1&0&0&3\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah kelima

$R_4 \rightarrow R_4 - R_3$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&1&1&1&12\\
0&0&0&-1&-1&-9\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah keenam

$R_4 \rightarrow -R_4$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&1&1&1&12\\
0&0&0&1&1&9\\
0&0&0&1&0&4
\end{array}
\right]$

## Langkah ketujuh

$R_5 \rightarrow R_5 - R_4$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&1&1&1&12\\
0&0&0&1&1&9\\
0&0&0&0&-1&-5
\end{array}
\right]$

## Langkah kedelapan

$R_5 \rightarrow -R_5$

$\left[
\begin{array}{ccccc|c}
1&1&1&1&1&15\\
0&1&1&1&1&14\\
0&0&1&1&1&12\\
0&0&0&1&1&9\\
0&0&0&0&1&5
\end{array}
\right]$

## Substitusi Mundur
$x_5 &= 5 
x_4 + x_5 &= 9  x_4 = 4 
x_3 + x_4 + x_5 &= 12 x_3 = 3 
x_2 + x_3 + x_4 + x_5 &= 14 x_2 = 2 
x_1 + x_2 + x_3 + x_4 + x_5 &= 15 x_1 = 1$

$(x_1,x_2,x_3,x_4,x_5) = (1,2,3,4,5)$

# Masukkan Code Di dalam
<iframe src="https://sagecell.sagemath.org/" width="1000" height="750"></iframe>
<script src="https://sagecell.sagemath.org/static/embedded_sagecell.js"></script>

<div class="sagecell">
<script type="text/x-sage">
var('x')
solve(x^2-4==0,x)
</script>
</div>

<script>
sagecell.makeSagecell({inputLocation: '.sagecell'});
</script>