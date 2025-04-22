<template>
	<view class="content">
		<view id="map" class="map"></view>
		<uni-popup ref="popup" border-radius="10px 10px 0 0">底部弹出 Popup 自定义圆角</uni-popup>
	</view>
</template>

<script>
	import "leaflet/dist/leaflet.css";
	import L, {
		latLng,
		latLngBounds
	} from "leaflet";
	import 'leaflet.offline'

	export default {
		data() {
			return {
				title: 'Hello'
			};
		},
		mounted() {
			//添加自定义图标
			var customIcon = L.icon({
				iconUrl: '/static/star.png',
				iconSize: [40, 40], // size of the icon
			});

			//添加图层,底图
			var baseLayer = L.tileLayer('/static/tiles/{z}/{x}/{y}.png', {
				minZoom: 3,
				maxZoom: 5, // 根据生成的层级调整
				tms: true, // 使用 TMS 瓦片坐标系统（Y轴反转）
				attribution: 'GPNU MCER',
				noWrap: true,
			});

			// 添加图层,标记
			var markLayer = L.layerGroup([
				L.marker([-64.5, 0.0]).setIcon(customIcon).bindPopup(
					'<h1>图书馆</h1><p><img src="/static/lib.png" width="100%" height="auto"></img><p>广东技术师范大学图书馆前身是原广东民族学院图书馆，创建于1957年。2002年和2005年分别与原广东省机械学校、原广东省经济管理干部学院和原广东省财贸管理干部学院图书馆合并，目前图书馆已形成“一校五馆”发展格局，馆舍总建筑面积约为8万平方米。'
					),
				L.marker([-58.0, 7.5]).setIcon(customIcon).bindPopup('第二教学楼'),
				L.marker([-80.0, -20.0]).setIcon(customIcon).bindPopup('正门'),
			]);

			// 初始化地图
			const map = L.map('map', {
				center: [-70.0, 0.0],
				zoom: 3,
				layers: [baseLayer, markLayer],
			})

			//设置最大边界，超出边界后会自动回弹
			map.setMaxBounds(latLngBounds(latLng(-90, -180), latLng(0, 180)));

			//添加图层选择控件
			var layerControl = L.control.layers({
				"渲染图": baseLayer
			}, {
				"标记": markLayer
			}).addTo(map);

		},
		methods: {}
	};
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	/* 设置地图容器的尺寸 */
	.map {
		width: 100%;
		height: 100vh;
		background: #5f5a56;
	}
</style>