(function () {
  'use strict';

  function safeText(value, limit) {
    return window.ARYSecurity.sanitizeText(String(value || ''), limit);
  }

  function safeAsset(value) {
    return window.ARYSecurity.sanitizeAssetUrl(value);
  }

  function renderPackages(data) {
    var grid = document.getElementById('grid-excursoes');
    if (!grid) return;
    var history = document.getElementById('historia-complementar-sr-ary');
    var complementaryHistory = data.config && safeText(data.config.historiaComplementarSrAry, 500);
    if (history && complementaryHistory) {
      history.textContent = complementaryHistory;
      history.classList.remove('hidden');
    }
    var now = new Date();
    var packages = Array.isArray(data.pacotes) ? data.pacotes : [];
    var visible = packages.filter(function (item) {
      if (!item || item.ativo !== true) return false;
      if (data.config && data.config.autoHideExpired === false) return true;
      return new Date(String(item.expiresAt || '') + 'T23:59:59') >= now;
    });
    grid.innerHTML = '';
    visible.forEach(function (item) {
      var card = document.createElement('article');
      card.className = 'excursion-card overflow-hidden rounded-3xl bg-white shadow-lg';
      var title = safeText(item.titulo, 100);
      var details = Array.isArray(item.itensInclusos) ? item.itensInclusos : [];
      card.innerHTML = '<img src="' + safeAsset(item.imagem) + '" alt="' +
        title + '" class="h-56 w-full object-cover">' +
        '<div class="p-6"><span class="fleet-badge">' + safeText(item.tipo, 60) + '</span>' +
        '<h3 class="mt-3 text-2xl font-black text-ary-primary">' + title + '</h3>' +
        '<p class="mt-3">' + safeText(item.descricao, 300) + '</p>' +
        '<p class="mt-3 font-semibold">' + safeText(item.saida, 120) + '</p>' +
        '<p class="mt-1 text-sm font-bold text-ary-primary">' + safeText(item.dataTexto, 120) + ' · ' +
        safeText(item.vagas, 60) + '</p><ul class="mt-4 list-disc pl-5 text-sm">' +
        details.map(function (detail) { return '<li>' + safeText(detail, 120) + '</li>'; }).join('') +
        '</ul><button type="button" class="mt-5 rounded-full bg-ary-primary px-5 py-3 font-bold text-white" data-excursion-message="' +
        safeText(item.mensagemWhatsapp, 500) + '">Consultar esta excursão</button></div>';
      grid.appendChild(card);
    });
    grid.querySelectorAll('[data-excursion-message]').forEach(function (button) {
      button.addEventListener('click', function () {
        var message = window.ARYSecurity.sanitizeText(button.getAttribute('data-excursion-message'), 500);
        var url = window.ARYSecurity.buildSafeWhatsAppUrl(
          data.config && data.config.whatsappPhone,
          { servico: 'Excursões e bate e volta', observacoes: message }
        );
        if (url) window.open(url, '_blank', 'noopener,noreferrer');
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    fetch('assets/data/excursoes.json', { cache: 'no-store' })
      .then(function (response) {
        if (!response.ok) throw new Error('Não foi possível carregar as excursões.');
        return response.json();
      })
      .then(renderPackages)
      .catch(function (error) {
        console.error('[ARY-EXCURSOES]', error);
      });
  });
})();
