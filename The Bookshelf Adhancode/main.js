const books = [];
const RENDER_EVENT = 'render-book';
const STORAGE_KEY = 'BOOKSHELF_APPS';
let editingBookId = null;
let searchQuery = '';

// Fungsi buat nampilin tanggal dinamis di Header (Vibe Koran)
function updateNewspaperDate() {
    const header = document.querySelector('header');
    if (header) {
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const today = new Date().toLocaleDateString('id-ID', options);
        header.setAttribute('data-date', `${today} - Edisi Terbaru`);
    }
}

function isStorageExist() {
    if (typeof(Storage) === undefined) {
        alert('Browser kamu tidak mendukung local storage');
        return false;
    }
    return true;
}

function saveData() {
    if (isStorageExist()) {
        const parsed = JSON.stringify(books);
        localStorage.setItem(STORAGE_KEY, parsed);
    }
}

function loadDataFromStorage() {
    const serializedData = localStorage.getItem(STORAGE_KEY);
    let data = JSON.parse(serializedData);

    if (data !== null) {
        for (const book of data) {
            books.push(book);
        }
    }
    document.dispatchEvent(new Event(RENDER_EVENT));
}

function makeBookElement(bookObject) {
    const { id, title, author, year, isComplete } = bookObject;

    const container = document.createElement('div');
    container.setAttribute('data-bookid', id);
    container.setAttribute('data-testid', 'bookItem');

    const titleEl = document.createElement('h3');
    titleEl.setAttribute('data-testid', 'bookItemTitle');
    titleEl.innerText = title;

    const authorEl = document.createElement('p');
    authorEl.setAttribute('data-testid', 'bookItemAuthor');
    authorEl.innerText = `Penulis: ${author}`;

    const yearEl = document.createElement('p');
    yearEl.setAttribute('data-testid', 'bookItemYear');
    yearEl.innerText = `Tahun: ${year}`;

    const actionContainer = document.createElement('div');

    const toggleBtn = document.createElement('button');
    toggleBtn.setAttribute('data-testid', 'bookItemIsCompleteButton');
    toggleBtn.innerText = isComplete ? 'Belum selesai dibaca' : 'Selesai dibaca';
    toggleBtn.addEventListener('click', () => {
        toggleBookComplete(id);
    });

    const deleteBtn = document.createElement('button');
    deleteBtn.setAttribute('data-testid', 'bookItemDeleteButton');
    deleteBtn.innerText = 'Hapus Buku';
    deleteBtn.addEventListener('click', () => {
        deleteBook(id);
    });

    const editBtn = document.createElement('button');
    editBtn.setAttribute('data-testid', 'bookItemEditButton');
    editBtn.innerText = 'Edit Buku';
    editBtn.addEventListener('click', () => {
        editBook(id);
    });

    actionContainer.append(toggleBtn, deleteBtn, editBtn);
    container.append(titleEl, authorEl, yearEl, actionContainer);

    return container;
}

function addOrUpdateBook() {
    const title = document.getElementById('bookFormTitle').value;
    const author = document.getElementById('bookFormAuthor').value;
    const year = Number(document.getElementById('bookFormYear').value);
    const isComplete = document.getElementById('bookFormIsComplete').checked;

    if (editingBookId !== null) {
        const bookIndex = books.findIndex((b) => b.id === editingBookId);
        if (bookIndex !== -1) {
            books[bookIndex] = {...books[bookIndex], title, author, year, isComplete };
        }
        editingBookId = null;
        document.getElementById('bookFormSubmit').innerText = 'Masukkan ke Rak';
    } else {
        const id = +new Date();
        books.push({ id, title, author, year, isComplete });
    }

    document.getElementById('bookForm').reset();
    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData();
}

function toggleBookComplete(bookId) {
    const bookTarget = books.find((b) => b.id === bookId);
    if (bookTarget == null) return;

    bookTarget.isComplete = !bookTarget.isComplete;
    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData();
}

function deleteBook(bookId) {
    const isConfirmed = confirm('Apakah Anda yakin ingin menghapus buku ini?');
    if (isConfirmed) {
        const bookIndex = books.findIndex((b) => b.id === bookId);
        if (bookIndex === -1) return;

        books.splice(bookIndex, 1);
        document.dispatchEvent(new Event(RENDER_EVENT));
        saveData();
    }
}

function editBook(bookId) {
    const bookTarget = books.find((b) => b.id === bookId);
    if (bookTarget == null) return;

    document.getElementById('bookFormTitle').value = bookTarget.title;
    document.getElementById('bookFormAuthor').value = bookTarget.author;
    document.getElementById('bookFormYear').value = bookTarget.year;
    document.getElementById('bookFormIsComplete').checked = bookTarget.isComplete;

    editingBookId = bookTarget.id;
    document.getElementById('bookFormSubmit').innerText = 'Simpan Perubahan';

    window.scrollTo({ top: 0, behavior: 'smooth' });
    document.getElementById('bookFormTitle').focus();
}

document.addEventListener('DOMContentLoaded', function() {
    updateNewspaperDate();

    const submitForm = document.getElementById('bookForm');
    submitForm.addEventListener('submit', function(event) {
        event.preventDefault();
        addOrUpdateBook();
    });

    const searchForm = document.getElementById('searchBook');
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        searchQuery = document.getElementById('searchBookTitle').value;
        document.dispatchEvent(new Event(RENDER_EVENT));
    });

    if (isStorageExist()) {
        loadDataFromStorage();
    }
});

document.addEventListener(RENDER_EVENT, function() {
    const incompleteList = document.getElementById('incompleteBookList');
    const completeList = document.getElementById('completeBookList');

    incompleteList.innerHTML = '';
    completeList.innerHTML = '';

    const booksToRender = books.filter((b) =>
        b.title.toLowerCase().includes(searchQuery.toLowerCase())
    );

    for (const bookItem of booksToRender) {
        const bookElement = makeBookElement(bookItem);
        if (!bookItem.isComplete) {
            incompleteList.append(bookElement);
        } else {
            completeList.append(bookElement);
        }
    }
});