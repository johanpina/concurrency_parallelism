
document.addEventListener('DOMContentLoaded', () => {
    const syncBtn = document.getElementById('sync-btn');
    const asyncBtn = document.getElementById('async-btn');
    const syncProgress = document.getElementById('sync-progress');
    const asyncProgress = document.getElementById('async-progress');

    syncBtn.addEventListener('click', () => {
        startDownload('sync', syncProgress, [syncBtn, asyncBtn]);
    });

    asyncBtn.addEventListener('click', () => {
        startDownload('async', asyncProgress, [syncBtn, asyncBtn]);
    });

    function startDownload(type, progressElement, buttons) {
        progressElement.innerHTML = '';
        buttons.forEach(btn => btn.disabled = true);

        const eventSource = new EventSource(`/${type}-download`);

        eventSource.onmessage = function(event) {
            console.log('Received event data:', event.data);
            try {
                const data = JSON.parse(event.data);

                if (data.status === 'completo') {
                    progressElement.innerHTML += '<div class="alert alert-info mt-2">Todas las descargas han finalizado.</div>';
                    eventSource.close();
                    buttons.forEach(btn => btn.disabled = false);
                    return;
                }

                const progressBar = `
                    <div class="progress mt-2">
                        <div class="progress-bar" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">
                            Archivo ${data.file} / ${data.total} - Contenido: ${data.content}
                        </div>
                    </div>`;
                progressElement.innerHTML += progressBar;
            } catch (e) {
                console.error('Error parsing JSON from EventSource:', e, 'Data received:', event.data);
                progressElement.innerHTML += `<div class="alert alert-danger mt-2">Error al procesar datos del servidor: ${e.message}. Datos: ${event.data}</div>`;
                eventSource.close();
                buttons.forEach(btn => btn.disabled = false);
            }
        };

        eventSource.onerror = function() {
            progressElement.innerHTML = '<div class="alert alert-danger mt-2">Error en la conexión.</div>';
            eventSource.close();
            buttons.forEach(btn => btn.disabled = false);
        };
    }
});

