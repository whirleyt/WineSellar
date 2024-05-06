from flask import Flask, render_template, request, abort, redirect, url_for, jsonify

app = Flask(__name__)

current_id = 4

wine = [
    {
        "id": 0,
        "title": "Flowers Pinot Noir",
        "winemaker": "Matt Barlowe",
        "vintage": 2012,
        "color": "red",
        "region": "Oregon",
        "body": "Light",
        "tannin": "Light",
        "acid": "Medium",
        "tasting_notes": ["dark cherry", "floral", "raspberry", "hint of oak", "earthy undertones", "spice"],
        "rating": 9.1,
        "other_regions": ["California", "France", "New Zealand", "Chile", "Australia"],
        "description": "Flowers Pinot Noir by Robert Cassette stands out as a quintessential example of the elegance and complexity "
                       +"Pinot Noir can achieve, particularly from Oregon. This wine showcases a light body with light tannins and medium "
                       +"acidity, creating a harmonious balance on the palate. The initial dark cherry and floral notes are complemented "
                       +"by layers of raspberry, a hint of oak, earthy undertones, and a touch of spice, offering a nuanced tasting "
                       +"experience. Revered for its versatility and sophistication, it has rightly earned a rating of 8.7, appealing to "
                       +"both connoisseurs and casual enthusiasts alike.",
        "image_url": "/static/images/flowers.jpg"
    },
    {
        "id": 1,
        "title": "Flowers Cabernet Sauvignon",
        "winemaker": "Matt Barlowe",
        "vintage": 2013,
        "color": "red",
        "region": "Oregon",
        "body": "Full",
        "tannin": "Heavy",
        "acid": "Light",
        "tasting_notes": ["dark cherry", "tobacco", "black currant", "leather", "vanilla", "hints of cedar"],
        "rating": 8.6,
        "other_regions": ["California", "France", "South Africa", "Argentina", "Italy"],
        "description": "Meticulously crafted by Robert Cassette, is a testament to the robust elegance and complexity achievable in "
                       + "Cabernet Sauvignon from Oregon. This full-bodied red wine, with heavy tannins and light acidity, presents a "
                       + "rich tapestry of flavors, from the initial notes of dark cherry and tobacco to deeper layers of black currant, "
                       + "leather, and vanilla, with subtle hints of cedar. It reflects the winemaker's dedication to excellence and the "
                       + "fertile terroirs of its origins, earning a distinguished rating of 8.6. This Cabernet Sauvignon is a true "
                       + "reflection of sophistication, designed to captivate the palates of enthusiasts and collectors alike.",
        "image_url": "/static/images/flowers-cab.jpg"
    },
    {
        "id": 2,
        "title": "Grapevine Pinot Noir",
        "winemaker": "Nick Reilly",
        "vintage": 2022,
        "color": "red",
        "region": "California",
        "body": "Light",
        "tannin": "Light",
        "acid": "Light",
        "tasting_notes": ["black raspberry", "almond", "red cherry", "vanilla", "subtle earthiness", "floral undertones"],
        "rating": 7,
        "other_regions": ["California", "France", "New Zealand", "Chile", "Australia"],
        "description": "Crafted with expertise by Nick Reilly, is a delicate yet complex wine originating from the renowned vineyards "
                       +"of Sonoma. This light-bodied Pinot Noir, with its light tannins and acidity, offers a refined palate of black "
                       +"raspberry and almond, complemented by notes of red cherry, vanilla, and a subtle earthiness, with floral "
                       +"undertones adding to its elegance. With a rating of 8.3, it represents a harmonious blend of tradition and the "
                       +"winemaker's distinctive approach to winemaking. 'Grape Vine Pinot Noir' is a testament to the beauty of Sonoma's "
                       +"terroir, inviting wine enthusiasts to explore its layered complexity.",
        "image_url": "/static/images/grapevine.webp"
    },
    {
        "id": 3,
        "title": "Milling Cabernet Franc",
        "winemaker": "Robert Lawrence",
        "vintage": 2019,
        "color": "red",
        "region": "France",
        "body": "Medium",
        "tannin": "Medium",
        "acid": "Light",
        "tasting_notes": ["grass", "stone fruit", "blackberry", "bell pepper", "graphite", "a hint of tobacco"],
        "rating": 10,
        "other_regions": ["California", "Italy", "Australia", "South Africa"],
        "description": "Crafted by the renowned Robert Chivoley, 'Milling Cabernet Franc' is a distinguished red wine that "
                       +"embodies the rich terroir of France. With a medium body, medium tannins, and light acidity, it presents a "
                       +"unique tasting profile of grass and stone fruit, indicative of its meticulous cultivation and production "
                       +"processes. This wine not only pays homage to its French origins through its complex flavors but also through "
                       +"its elegantly designed label that reflects both tradition and modernity. Rated 9.1, it stands as a testament "
                       +"to the craftsmanship and heritage of French winemaking, appealing to connoisseurs worldwide.",
        "image_url": "/static/images/milling.webp"
    },
    {
        "id": 4,
        "title": "Stiving Cabernet Franc",
        "winemaker": "Tara Steil",
        "vintage": 2018,
        "color": "red",
        "region": "France",
        "body": "Light",
        "tannin": "Light",
        "acid": "Medium",
        "tasting_notes": ["tobacco", "blackberry", "plum", "green pepper", "hints of vanilla", "earthy undertones"],
        "rating": 8,
        "other_regions": ["California", "Italy", "Australia", "South Africa"],
        "description": "Stiving Cabernet Franc by Tara Steil is an exquisite red wine that showcases the finesse achievable with "
                       +"Cabernet Franc in France. Characterized by a light body, light tannins, and medium acidity, it reveals a "
                       +"sophisticated palette that starts with tobacco and blackberry and unfolds to reveal plum, green pepper, "
                       +"and hints of vanilla with earthy undertones. This wine, with a rating of 8.1, stands as a tribute to the "
                       +"versatility of Cabernet Franc, reflecting the meticulous care in its crafting. Stiving Cabernet Franc "
                       +"is a celebration of both the tradition and innovation in winemaking, appealing to those who appreciate subtlety"
                       +" and depth in their wine.",
        "image_url": "/static/images/stiving.webp"
    },
    {
        "id": 5,
        "title": "Alamo Malbec",
        "winemaker": "Steve Cam",
        "vintage": 2023,
        "color": "red",
        "region": "Argentina",
        "body": "Full",
        "tannin": "Medium",
        "acid": "Light",
        "tasting_notes": ["minerality", "red fruit", "dark chocolate", "plum", "subtle floral aroma"],
        "rating": 6,
        "other_regions": ["California", "France"],
        "description": "Alamo Malbec by Steve Cam is a full-bodied red wine that beautifully encapsulates the essence of Argentina's "
                       +"terroir. With medium tannins and light acidity, it presents a complex palette of minerality and red fruit, "
                       +"enriched with notes of dark chocolate, plum, and a subtle floral aroma. This Malbec, rated at 7.8, is a "
                       +"vibrant testament to Argentina's rich wine culture, combining traditional and modern elements in both its "
                       +"flavor and design. It's a celebration of the meticulous craftsmanship that Steve Cam brings to winemaking, "
                       +"appealing to those who appreciate depth and complexity in their wine.",
        "image_url": "/static/images/alamo.webp"
    },
    {
        "id": 6,
        "title": "Rabbit Malbec",
        "winemaker": "Sam Hilling",
        "vintage": 2013,
        "color": "red",
        "region": "Argentina",
        "body": "Medium",
        "tannin": "Light",
        "acid": "Medium",
        "tasting_notes": ["liquorice", "blackberry", "mocha", "leather", "hint of peppermint"],
        "rating": 8,
        "other_regions": ["California", "France"],
        "description": "Rabbit Malbec by Sam Hilling is a masterfully created wine that embodies the rich essence of Argentina's "
                       +"wine-making tradition. With a medium body, light tannins, and medium acidity, it offers a palate of liquorice "
                       +"and blackberry, further enhanced by notes of mocha, leather, and a hint of peppermint, adding layers of "
                       +"complexity. Rated at 8.5, this Malbec is a homage to the skilled craft of Sam Hilling and the vibrant "
                       +"landscapes of Argentina, designed to captivate wine lovers around the globe with its unique blend of "
                       +"traditional and modern flavors.",
        "image_url": "/static/images/rabbit.webp"
    },
    {
        "id": 7,
        "title": "Golden Apple Chardonnay",
        "winemaker": "Robert Stanley",
        "vintage": 2022,
        "color": "white",
        "region": "California",
        "body": "Full",
        "tannin": "Light",
        "acid": "Medium",
        "tasting_notes": ["apple", "cinnamon", "citrus", "vanilla", "touch of oak"],
        "rating": 9.3,
        "other_regions": ["France", "New York", "Washington"],
        "description": "'Golden Apple Chardonnay' by Robert Stanley is a full-bodied white wine that captures the essence of "
                       +"California's rich viticultural heritage. With light tannins and medium acidity, it offers a delightful "
                       +"palate of apple and cinnamon, enhanced by layers of citrus, vanilla, and a touch of oak. Rated at 9.3, "
                       +"this Chardonnay is a testament to the skillful art of winemaking, blending traditional flavors with "
                       +"innovative techniques. It's a tribute to the sophistication and diversity of Californian wine, designed "
                       +"to enchant wine lovers with its complexity and elegance.",
        "image_url": "/static/images/apple.webp"
    },
    {
        "id": 8,
        "title": "Orange Valley Chardonnay",
        "vintage": 2023,
        "winemaker": "Kaci Lynne",
        "color": "white",
        "region": "California",
        "body": "Light",
        "tannin": "Light",
        "acid": "Medium",
        "tasting_notes": ["orange blossom", "lemon", "peach", "melon", "subtle minerality"],
        "rating": 9.1,
        "other_regions": ["France", "New York", "Washington"],
        "description": "Orange Valley Chardonnay by Kaci Lynne captures the essence of a Californian summer with its light "
                       +"and refreshing profile. Featuring light tannins and medium acidity, it delivers a delightful blend of "
                       +"orange blossom, lemon, peach, and melon, with a hint of minerality. Rated at 9.1, this Chardonnay celebrates "
                       +"the vibrant viticulture of California, melding traditional winemaking with a modern twist to enchant wine "
                       +"enthusiasts. Its label, reflecting the sunny valleys and aromatic freshness, invites a taste of California's "
                       +"finest.",
        "image_url": "/static/images/orange-valley.webp"
    },
    {
        "id": 9,
        "title": "Amset Sauvignon Blanc",
        "vintage": 2023,
        "winemaker": "Pete Stan",
        "color": "white",
        "region": "New Zealand",
        "body": "Light",
        "tannin": "Light",
        "acid": "High",
        "tasting_notes": ["grass", "grapefruit", "passion fruit", "lime", "hint of minerality"],
        "rating": 8.2,
        "other_regions": ["California", "Chile", "South Africa", "Australia"],
        "description": "Amset Sauvignon Blanc by Pete Stan is a tribute to the unique terroir of New Zealand, offering a light-bodied "
                       +"wine with high acidity and a vibrant blend of grass, grapefruit, passion fruit, and lime, with a hint of "
                       +"minerality. Rated at 8.2, this Sauvignon Blanc captures the essence of New Zealand's pristine wine regions, "
                       +"delivering a crisp and refreshing experience that reflects the winemaker's skill and dedication. Its label, "
                       +"inspired by the dynamic landscapes of New Zealand, combines bright colors and modern design, making it not "
                       +"just a wine, but a piece of art that appeals to wine enthusiasts around the globe.",
        "image_url": "/static/images/amset.webp"
    },
    {
        "id": 10,
        "title": "Rain Sauvignon Blanc",
        "vintage": 2022,
        "winemaker": "Robert Pete",
        "color": "white",
        "region": "California",
        "body": "Light",
        "tannin": "Light",
        "acid": "High",
        "tasting_notes": ["apple", "citrus", "melon", "pear", "crisp minerality"],
        "rating": 7.2,
        "other_regions": ["New Zealand", "Chile", "South Africa", "Australia"],
        "description": "Rain Sauvignon Blanc by Robert Pete is a light-bodied white wine that epitomizes the vibrant character of "
                       +"California's terroir. With high acidity and light tannins, it presents a refreshing palate of apple and "
                       +"citrus, enhanced by notes of melon, pear, and crisp minerality. Rated at 8.8, this Sauvignon Blanc is a "
                       +"testament to the meticulous craftsmanship of Robert Pete, blending traditional wine-making techniques with "
                       +"a modern aesthetic. It's a celebration of California's winemaking prowess, designed to delight the senses "
                       +"with its purity and zest.",
        "image_url": "/static/images/rain.webp"
    }
]



# ROUTES

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower().strip()

    def matches_query(item):
        if query in item['title'].lower() \
                or query in item['color'].lower() \
                or query in item['winemaker'].lower()\
                or query in item['region'].lower():
            return True
        for note in item['tasting_notes']:
            if query in note.lower():
                return True
        return False

    matching_items = [item for item in wine if matches_query(item)]
    return render_template('search_results.html', query=query, items=matching_items)

@app.route('/view/<int:item_id>')
def view_item(item_id):
    item = next((item for item in wine if item["id"] == item_id), None)
    if item is not None:
        return render_template('item_detail.html', item=item)
    else:
        abort(404)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_item = {
            "id": len(wine),
            "title": request.form['title'],
            "winemaker": request.form['winemaker'],
            "vintage": request.form['vintage'],
            "color": request.form['color'],
            "region": request.form['region'],
            "body": request.form['body'],
            "tannin": request.form['tannin'],
            "acid": request.form['acid'],
            "tasting_notes": request.form.getlist('tasting_notes'),
            "rating": request.form['rating'],
            "description": request.form['description'],
            "image_url": request.form['image_url'],
            "other_regions": request.form.getlist('other_regions')
        }
        wine.append(new_item)
        return jsonify({"itemId": new_item["id"], "message": "New item successfully created."})
    return render_template('add_item.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = next((item for item in wine if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404

    if request.method == 'POST':
        item['id']= item_id
        item['title'] = request.form['title']
        item['winemaker'] = request.form['winemaker']
        item['vintage'] = int(request.form['vintage'])
        item['color'] = request.form['color']
        item['region'] = request.form['region']
        item['body'] = request.form['body']
        item['tannin'] = request.form['tannin']
        item['acid'] = request.form['acid']
        item['tasting_notes'] = request.form['tasting_notes'].split(', ')
        item['rating'] = float(request.form['rating'])
        item['other_regions'] = request.form['other_regions'].split(', ')
        item['description'] = request.form['description']
        item['image_url'] = request.form['image_url']

        return redirect(url_for('view_item', item_id=item_id))

    return render_template('edit_item.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, port=8080)