def get_single_rec_html(rec):
    return '''
    <div style="display:flex;flex-direction:column;gap:20px;background-color:grey;box-sizing:border-box;
    padding:20px;border-radius: 8px;font-family:Roboto,Helvetica,serif;color:white;">
        <div style="font-size:20px;">{}</div>
        <div style="font-size:14px;">{}</div>
        <div style="font-size:32px;">{}</div>
    </div>
    '''.format(rec['title'], rec['text'], rec['price'])


def wrap_with_global_styles(data: str) -> str:
    return '''
    <div style="width:calc(100vw - 16px);height:calc(100vh - 16px);display:flex;align-items:center;
    justify-content:center;gap:10px;">
    {}
    </div>
    '''.format(data)
