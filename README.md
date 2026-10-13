# Tower of Hanoi dengan Python

## Deskripsi Program

Program ini merupakan implementasi permainan Tower of Hanoi menggunakan bahasa pemrograman Python. Tujuan permainan adalah memindahkan seluruh cakram dari tiang awal ke tiang tujuan dengan bantuan satu tiang tambahan.

## Tujuan Program

Program dibuat untuk memahami penggunaan fungsi, list, rekursi, dan manipulasi data dalam Python melalui simulasi pemindahan cakram.

## Penjelasan Kode

### 1. Fungsi `main_py(no_list)`

Fungsi utama menerima parameter `no_list` yang menentukan jumlah cakram. List `A` digunakan sebagai tiang awal, `B` sebagai tiang bantuan, dan `C` sebagai tiang tujuan.

### 2. Fungsi `getList_string()`

Fungsi ini menghasilkan representasi kondisi ketiga tiang dalam bentuk string. Kondisi tersebut ditampilkan setiap kali cakram selesai dipindahkan.

### 3. Fungsi `move_rings(start, goal)`

Fungsi ini memindahkan satu cakram dari tiang awal ke tiang tujuan menggunakan operasi `pop()` dan `append()`. Operasi `pop()` mengambil cakram paling atas, sedangkan `append()` menambahkan cakram ke tiang tujuan.

### 4. Fungsi `move_stick(start, goal, auxiliary, n)`

Fungsi ini menggunakan rekursi untuk memindahkan cakram. Jika jumlah cakram adalah satu, cakram langsung dipindahkan ke tiang tujuan. Jika jumlahnya lebih dari satu, program memindahkan cakram bagian atas ke tiang bantuan, memindahkan cakram terbesar ke tujuan, kemudian memindahkan kembali cakram yang berada di tiang bantuan ke tujuan.

### 5. Pemanggilan Program

Perintah `print(main_py(3))` menjalankan program dengan tiga cakram. Hasilnya berupa urutan kondisi tiang selama proses pemindahan berlangsung.

## Algoritma yang Digunakan

Algoritma yang digunakan adalah rekursi. Rekursi merupakan teknik pemrograman ketika sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan permasalahan yang lebih kecil hingga mencapai kondisi dasar (*base case*).

## Kesimpulan

Program Tower of Hanoi menunjukkan penerapan rekursi dan manipulasi list dalam Python. Melalui program ini, proses pemindahan cakram dapat dilakukan secara bertahap sampai seluruh cakram berada pada tiang tujuan.
