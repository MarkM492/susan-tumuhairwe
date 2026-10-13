/* Skyline Blueprint: inline SVG icon sprite.
   Usage:  <svg class="icon" aria-hidden="true"><use href="#i-search"></use></svg>
   The sprite is injected once, so pages work from file:// and need no extra request.
   Line icons (tiles) are stroked; glyph icons (social, contact) are filled. */
(function () {
  var S = 'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"';
  var sym = {
    /* Tile / feature icons (line) */
    'plane':       '<path ' + S + ' d="M21 15.500v-1.800L13.500 9V4a1.500 1.500 0 00-3 0v5L3 13.700v1.800l7.500-2.300V18l-2 1.500V21l3.500-1 3.500 1v-1.500l-2-1.500v-4.800z"/>',
    'plane-takeoff':'<path ' + S + ' d="M3 20h18M3.500 12.800l2.700-1.200 3.600.900 6.200-3a2 2 0 011.700 3.600l-6.700 3.400-4.700-.3-2.600-1.100z"/>',
    'shield-check':'<path ' + S + ' d="M12 3l8 3v5.500c0 4.700-3.300 8.300-8 9.500-4.700-1.200-8-4.800-8-9.500V6z"/><path ' + S + ' d="M8.500 12l2.500 2.500 4.500-5"/>',
    'compass':     '<circle ' + S + ' cx="12" cy="12" r="9"/><path ' + S + ' d="M15.500 8.500l-1.800 5.200-5.200 1.800 1.800-5.200z"/><path ' + S + ' d="M5.600 18.400L18.400 5.600"/>',
    'calendar-plane':'<rect ' + S + ' x="3.500" y="5" width="17" height="15.500" rx="2"/><path ' + S + ' d="M3.500 10h17M8 3v4M16 3v4M9 17l6-5"/><path ' + S + ' d="M13 12.500l2.500-.5-.5 2.500"/>',
    'book':        '<path ' + S + ' d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2zM4 19a2 2 0 012-2h13"/>',
    'target':      '<circle ' + S + ' cx="12" cy="12" r="9"/><circle ' + S + ' cx="12" cy="12" r="4.500"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    'edit':        '<path ' + S + ' d="M4 20h4L19 9l-4-4L4 16zM13.500 6.500l4 4"/>',
    'chart':       '<path ' + S + ' d="M4 20V4M4 20h16M8 15l3-4 3 2 5-6"/>',
    'users':       '<circle ' + S + ' cx="9" cy="8" r="3.500"/><path ' + S + ' d="M2.500 20a6.500 6.500 0 0113 0M16 4.500a3.500 3.500 0 010 7M18 14a6 6 0 013.500 5.500"/>',
    'lightbulb':   '<path ' + S + ' d="M9 18h6M10 21h4M12 3a6 6 0 00-3.500 10.900c.600.500 1 1.200 1 2.100h5c0-.900.400-1.600 1-2.100A6 6 0 0012 3z"/>',

    'calendar':    '<rect ' + S + ' x="3.500" y="5" width="17" height="15.500" rx="2"/><path ' + S + ' d="M3.500 10h17M8 3v4M16 3v4M8 14h2M13 14h3"/>',
    'heart':       '<path ' + S + ' d="M12 20.500S4 15.800 4 9.800A4.300 4.300 0 0112 7.700a4.300 4.300 0 018 2.100c0 6-8 10.700-8 10.700z"/>',
    'leaf':        '<path ' + S + ' d="M5 20C5 11 10 5 20 4c0 10-5 16-13 16M5 20c1.500-4 4-7.500 8-10"/>',
    'sprout':      '<path ' + S + ' d="M12 21v-8M12 13c0-4-3-6-7-6 0 4 3 6 7 6zM12 15c0-3.500 2.500-6 7-6 0 3.500-2.500 6-7 6z"/>',
    'mic':         '<rect ' + S + ' x="9" y="3" width="6" height="11" rx="3"/><path ' + S + ' d="M5.500 11a6.500 6.500 0 0013 0M12 17.500V21M9 21h6"/>',
    'bowl':        '<path ' + S + ' d="M3.500 11h17a8.500 8.500 0 01-17 0zM8 7c0-1 1-1.500 1-2.500M12 7c0-1 1-1.500 1-2.500M16 7c0-1 1-1.500 1-2.500M9 20.500h6"/>',
    'chat':        '<path ' + S + ' d="M4 5h16v11H10l-4 4v-4H4z"/>',
    'coins':       '<ellipse ' + S + ' cx="12" cy="6" rx="7" ry="3"/><path ' + S + ' d="M5 6v6c0 1.700 3 3 7 3s7-1.300 7-3V6M5 12v6c0 1.700 3 3 7 3s7-1.300 7-3v-6"/>',

    /* UI (stroke) */
    'menu':        '<path ' + S + ' d="M4 7h16M4 12h16M4 17h16"/>',
    'close':       '<path ' + S + ' d="M6 6l12 12M18 6L6 18"/>',
    'chevron-right':'<path ' + S + ' d="M9 5l7 7-7 7"/>',
    'chevron-down':'<path ' + S + ' d="M5 9l7 7 7-7"/>',
    'chevron-up':  '<path ' + S + ' d="M5 15l7-7 7 7"/>',
    'arrow-right': '<path ' + S + ' d="M4 12h16M14 6l6 6-6 6"/>',
    'arrow-up':    '<path ' + S + ' d="M12 20V5M6 11l6-6 6 6"/>',
    'download':    '<path ' + S + ' d="M12 4v11M7 11l5 5 5-5M5 20h14"/>',
    'file':        '<path ' + S + ' d="M7 3h7l5 5v13H7zM14 3v5h5"/>',
    'clock':       '<circle ' + S + ' cx="12" cy="12" r="9"/><path ' + S + ' d="M12 7v5l3 2"/>',
    'home':        '<path ' + S + ' d="M4 11l8-7 8 7v9a1 1 0 01-1 1h-4v-6H9v6H5a1 1 0 01-1-1z"/>',
    'mail':        '<rect ' + S + ' x="3" y="5" width="18" height="14" rx="2"/><path ' + S + ' d="M3.500 7l8.500 6 8.500-6"/>',

    /* Glyphs (fill) */
    'search':      '<path fill="currentColor" d="M10 3a7 7 0 105.200 11.700l4.500 4.500-1.400 1.400-4.500-4.500A7 7 0 0010 3zm0 2a5 5 0 110 10 5 5 0 010-10z"/>',
    'phone':       '<path fill="currentColor" d="M6.600 10.800a15.100 15.100 0 006.600 6.600l2.200-2.200a1 1 0 011-.250 11.400 11.400 0 003.600.600 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.500a1 1 0 011 1c0 1.300.200 2.500.600 3.600a1 1 0 01-.250 1z"/>',
    'pin':         '<path fill="currentColor" d="M12 2a7 7 0 00-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 00-7-7zm0 9.500A2.500 2.500 0 119.500 9a2.500 2.500 0 012.500 2.500z"/>',
    'x':           '<path fill="currentColor" d="M18.200 2H21l-6.500 7.400L22 22h-6l-4.700-6.100L5.800 22H3l7-8L2 2h6.100l4.200 5.600zm-1 18h1.600L7 3.800H5.300z"/>',
    'facebook':    '<path fill="currentColor" d="M14 8V6.500c0-.700.200-1 1.200-1H17V2h-2.800C11.200 2 10 3.700 10 6.200V8H8v3.500h2V22h4V11.500h2.700L17 8z"/>',
    'linkedin':    '<path fill="currentColor" d="M4.500 8.500h3V20h-3zM6 3.500a1.800 1.800 0 110 3.600 1.800 1.800 0 010-3.600zM10 8.500h2.900v1.600c.400-.800 1.500-1.800 3.200-1.800 3.400 0 4 2.200 4 5.100V20h-3v-5.700c0-1.400 0-3.100-1.900-3.100s-2.200 1.500-2.200 3V20h-3z"/>',
    'instagram':   '<path fill="currentColor" d="M7.500 2h9A5.500 5.500 0 0122 7.500v9a5.500 5.500 0 01-5.500 5.500h-9A5.500 5.500 0 012 16.500v-9A5.500 5.500 0 017.500 2zm0 2A3.500 3.500 0 004 7.500v9A3.500 3.500 0 007.500 20h9a3.500 3.500 0 003.500-3.500v-9A3.500 3.500 0 0016.500 4zM12 7a5 5 0 110 10 5 5 0 010-10zm0 2a3 3 0 100 6 3 3 0 000-6zm5.200-3.200a1.200 1.200 0 110 2.400 1.200 1.200 0 010-2.400z"/>',
    'youtube':     '<path fill="currentColor" d="M21.600 7.200a2.500 2.500 0 00-1.800-1.800C18.200 5 12 5 12 5s-6.200 0-7.800.4A2.500 2.500 0 002.400 7.200C2 8.800 2 12 2 12s0 3.200.4 4.800a2.500 2.500 0 001.800 1.800C5.800 19 12 19 12 19s6.200 0 7.800-.4a2.500 2.500 0 001.800-1.800c.4-1.600.4-4.800.4-4.800s0-3.200-.4-4.800zM10 15V9l5.200 3z"/>'
  };
  var out = '<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>';
  Object.keys(sym).forEach(function (k) {
    out += '<symbol id="i-' + k + '" viewBox="0 0 24 24">' + sym[k] + '</symbol>';
  });
  out += '</defs></svg>';
  function inject() { document.body.insertAdjacentHTML('afterbegin', out); }
  if (document.body) inject(); else document.addEventListener('DOMContentLoaded', inject);
})();
