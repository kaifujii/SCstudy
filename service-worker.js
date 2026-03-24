const CACHE_NAME = 'studydeck-v5';
const STATIC_ASSETS = [
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
  './sc/data/ch01.js',
  './sc/data/ch02.js',
  './sc/data/ch03.js',
  './sc/data/ch04.js',
  './sc/data/ch05.js',
  './sc/data/ch06.js',
  './sc/data/ch08.js',
  './sc/data/ch09.js',
];

// インストール時に静的アセットをキャッシュ
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
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

// HTMLはネットワーク優先（更新が即反映）、それ以外はキャッシュ優先
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  const isHTML = url.pathname.endsWith('.html') || url.pathname.endsWith('/');

  if (isHTML) {
    // Network first: 常に最新HTMLを取得、失敗時のみキャッシュ
    event.respondWith(
      fetch(event.request)
        .then((res) => {
          const clone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          return res;
        })
        .catch(() => caches.match(event.request))
    );
  } else {
    // Cache first: 静的アセットはキャッシュ優先
    event.respondWith(
      caches.match(event.request).then((cached) => cached || fetch(event.request))
    );
  }
});
