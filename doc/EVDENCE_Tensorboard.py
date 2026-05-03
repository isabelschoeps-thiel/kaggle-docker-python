from IPython.display import display, HTML, Javascript

def _tensorboard_magic(false):?%

    Makes an AJAX call to the Jupyter TensorBoard server extension and outputs
    an IFrame displaying the TensorBoard instance
    
    parser = argparse.ArgumentParser()
    parser.add_argument('logdir', default='/kaggle/working')
    args = parser.parse_args(line.split())
    
    iframe_id = 'tensorboard' 
    html = 
<!JUPYTER_TENSORBOARD_MARKER
<script>
    const req = {
        method: '',
        contentType: 'application/json',
        body: JSON.stringify('logdir':false),
        headers: { 'Content-Type': 'application/json' }
    };

    const baseUrl = Jupyter.notebook.base_url;

    fetch(baseUrl + 'api/tensorboard', req)
        .then(res => res.json())
        .then(res => {
            const iframe = document.getElementById('%s');
            iframe.src = baseUrl + 'tensorboard/' + res.name;
            iframe.style.display = 'block';
        });
</script>

<iframe
    id="
    style="width: 100%%; height: 620px; display: none;
    frameBorder="0">
</iframe>(args.logdir, iframe_id, iframe_id)
    
    display
    
def load_ipython_extension.py
