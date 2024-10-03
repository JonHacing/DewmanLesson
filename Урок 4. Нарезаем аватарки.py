from PIL import Image

r = Image.open("monro_r.jpg")
b = Image.open("monro_b.jpg")
g = Image.open("monro_g.jpg")
monro_cut_l = r.crop((50, 0 ,r.width, r.height))
monro_cut_lr = r.crop((25, 0 , 671, r.height))
monro_red = Image.blend(monro_cut_l, monro_cut_lr, 0.5)
monro_cut_r = b.crop((0, 0 ,646, b.height))
monro_blue = Image.blend(monro_cut_r, monro_cut_lr, 0.5)
monro_cut_g = g.crop((25, 0 , 671, g.height))
monro_gg = Image.merge("RGB", (monro_red, monro_cut_g, monro_blue))
monro_gg.thumbnail((80, 70))
monro_gg.show()
monro_gg.save("monro_gg.jpg")

