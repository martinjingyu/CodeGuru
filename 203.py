from flask import Flask, jsonify, request
import psycopg2
import websocket
import threading

app = Flask(__name__)

def get_device_info(ws_url):
    def on_message(ws, message):
        # Logic to handle WebSocket messages
        print("Message received: ", message)
        # Assuming the message is JSON and contains device info
        return message

    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message)
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.start()
    ws_thread.join()
    ws.close()

@app.route('/get_device_info_and_traffic', methods=['GET'])
def get_device_info_and_traffic():
    device_id = request.args.get('device_id')
    ws_url = request.args.get('ws_url')
    db_name = request.args.get('db_name')
    user = request.args.get('user')
    password = request.args.get('password')

    device_info = get_device_info(ws_url)

    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password
        )
        cur = conn.cursor()
        
        # Insecure SQL query with direct concatenation
        query = f"SELECT traffic_volume FROM traffic WHERE device_id = '{device_id}'"
        cur.execute(query)
        traffic_volume = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if traffic_volume:
            traffic_volume = traffic_volume[0]
        else:
            traffic_volume = None

        return jsonify({
            'device_info': device_info,
            'traffic_volume': traffic_volume
        })

    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)