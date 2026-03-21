const CACHE_NAME = 'sc-tango-v13';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-mono.svg',
  './icons/ui/card.svg',
  './icons/ui/list.svg',
  './icons/ui/shuffle.svg',
  './icons/ui/filter.svg',
  './icons/ui/refresh.svg',
  './icons/ui/book.svg',
  './icons/ui/search.svg',
  './icons/ui/pointer.svg',
  './icons/ui/moon.svg',
  './icons/ui/sun.svg',
  './icons/ui/close.svg',
  './icons/ui/chevron-down.svg',
  './icons/ui/check.svg',
  './icons/ui/arrow-left.svg',
  './icons/ui/arrow-right.svg',
  './data/ch01.js',
  './data/ch02.js',
  './data/ch03.js',
  './data/ch04.js',
  './data/ch05.js',
  './data/ch06.js',
  './data/ch08.js',
  './data/ch09.js',
];

// インストール時に全アセットをキャッシュ
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// 古いキャッシュを削除
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// キャッシュ優先、なければネットワーク取得
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
