<template>
  <view class="content">
    <view id="map" class="map"></view>
  </view>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
  data() {
    return {
      title: 'Hello'
    };
  },
  mounted() {
    // 初始化地图
    const map = L.map('map').setView([-70.0, 0.0], 5);

    L.tileLayer('/static/tiles/{z}/{x}/{y}.png', {
	  minZoom: 1, 
	  maxZoom: 5, // 根据生成的层级调整
	  tms: true, // 使用 TMS 瓦片坐标系统（Y轴反转）
	  attribution: 'GPNU MCER'
    }).addTo(map);

    // 添加标记,图书馆
    L.marker([-64.5, 0.0]).addTo(map)
      .bindPopup('白云校区图书馆')
      .openPopup();
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
  height: 100vh; /* 根据需求调整 */
}

/* 其他样式（如 logo、text-area 等）可保留 */
</style>