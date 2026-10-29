(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var menuButton = document.querySelector('[data-menu-toggle]');
    var menu = document.querySelector('[data-mobile-menu]');
    if (menuButton && menu) {
      menuButton.addEventListener('click', function () {
        var expanded = menuButton.getAttribute('aria-expanded') === 'true';
        menuButton.setAttribute('aria-expanded', String(!expanded));
        menu.classList.toggle('is-open', !expanded);
      });
    }

    var whatsappToggle = document.querySelector('[data-whatsapp-toggle]');
    var whatsappOptions = document.querySelector('[data-whatsapp-options]');
    if (whatsappToggle && whatsappOptions) {
      whatsappToggle.addEventListener('click', function () {
        var expanded = whatsappToggle.getAttribute('aria-expanded') === 'true';
        whatsappToggle.setAttribute('aria-expanded', String(!expanded));
        whatsappOptions.hidden = expanded;
      });
      document.addEventListener('click', function (event) {
        if (!event.target.closest('.whatsapp-contact')) {
          whatsappToggle.setAttribute('aria-expanded', 'false');
          whatsappOptions.hidden = true;
        }
      });
    }

    var filters = document.querySelectorAll('[data-filter]');
    var cards = document.querySelectorAll('[data-category]');
    filters.forEach(function (button) {
      button.addEventListener('click', function () {
        filters.forEach(function (item) { item.classList.remove('is-active'); });
        button.classList.add('is-active');
        var filter = button.getAttribute('data-filter');
        cards.forEach(function (card) {
          card.hidden = filter !== 'todos' && card.getAttribute('data-category') !== filter;
        });
      });
    });

    var modal = document.querySelector('[data-lightbox]');
    var modalImage = modal && modal.querySelector('img');
    var closeModal = function () {
      if (modal) modal.hidden = true;
    };
    document.querySelectorAll('[data-lightbox-src]').forEach(function (trigger) {
      trigger.addEventListener('click', function () {
        if (!modal || !modalImage) return;
        modalImage.src = trigger.getAttribute('data-lightbox-src');
        modalImage.alt = trigger.getAttribute('alt') || 'Imagem ampliada da frota';
        modal.hidden = false;
        if (modalImage.focus) modalImage.focus();
      });
    });
    if (modal) {
      modal.addEventListener('click', function (event) {
        if (event.target === modal || event.target.hasAttribute('data-lightbox-close')) closeModal();
      });
    }
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeModal();
    });
    var year = document.querySelector('[data-current-year]');
    if (year) year.textContent = String(new Date().getFullYear());
  });
})();
