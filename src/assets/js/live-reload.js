(function () {
  'use strict';

  var lastMtime = null;
  var polling = false;

  function checkForChanges() {
    if (polling) return;
    polling = true;
    fetch('/__mtime', { cache: 'no-store' })
      .then(function (response) {
        if (!response.ok) throw new Error('Falha ao consultar o estado dos arquivos.');
        return response.json();
      })
      .then(function (payload) {
        if (lastMtime === null) {
          lastMtime = payload.mtime;
          return;
        }
        if (payload.mtime !== lastMtime) {
          window.location.reload();
        }
      })
      .catch(function (error) {
        console.warn('[ARY-LIVE-RELOAD] Falha ao consultar /__mtime:', error);
      })
      .finally(function () {
        polling = false;
      });
  }

  checkForChanges();
  window.setInterval(checkForChanges, 1000);
})();
