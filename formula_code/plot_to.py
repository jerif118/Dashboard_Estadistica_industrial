import io
import base64
def plot_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_bytes = buf.getvalue()
    buf.close()
    return base64.b64encode(img_bytes).decode('utf-8')

