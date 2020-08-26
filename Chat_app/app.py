from flask import Flask , render_template , request, jsonify
import pusher


   
app = Flask(__name__,template_folder='templates')

pusher_client = pusher.Pusher(
    app_id='946542',
    key='d417f479a3ef2af3f3a6',
    secret='bd91be397fb6697dd006',
    cluster='ap2',
    ssl=True
    )

@app.route('/',methods=["GET","POST"])
def home():
        return render_template('chat_app.html')

@app.route('/message',methods=["POST"])
def message():
   try:
            username = request.form.get('username')
            message = request.form.get('message')
            pusher_client.trigger('my-channel', 'send-message', {'username':username,'message': message})
            return jsonify({'result':'success'})
   except:
            return jsonify({'result':'failed'})

if __name__ == '__main__':
    app.run()
