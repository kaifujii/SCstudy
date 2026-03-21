const CACHE_NAME = 'studydeck-v3';
const ASSETS = [
  './',
  './index.html',
  './sc/manifest.json',
  './sc/icons/icon-192.png',
  './sc/icons/icon-512.png',
  './sc/icons/icon-mono.svg',
  './sc/icons/ui/card.svg',
  './sc/icons/ui/list.svg',
  './sc/icons/ui/shuffle.svg',
  './sc/icons/ui/filter.svg',
  './sc/icons/ui/refresh.svg',
  './sc/icons/ui/book.svg',
  './sc/icons/ui/search.svg',
  './sc/icons/ui/pointer.svg',
  './sc/icons/ui/moon.svg',
  './sc/icons/ui/sun.svg',
  './sc/icons/ui/close.svg',
  './sc/icons/ui/chevron-down.svg',
  './sc/icons/ui/check.svg',
  './sc/icons/ui/arrow-left.svg',
  './sc/icons/ui/arrow-right.svg',
  './sc/flashcard.html',
  './sc/data/ch01.js',
  './sc/data/ch02.js',
  './sc/data/ch03.js',
  './sc/data/ch04.js',
  './sc/data/ch05.js',
  './sc/data/ch06.js',
  './sc/data/ch08.js',
  './sc/data/ch09.js',
  './az305/index.html',
  './az305/vol1.html',
  './az305/vol2.html',
  './az305/vol3.html',
  './az305/vol4.html',
  './az305/vol5.html',
  './az305/az305.css',
  './az305/az305-vol1.css',
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
