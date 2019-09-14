package com.htn.proj;

import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;
import android.view.View;

public class GeoListener implements LocationListener {
    @Override
    public void onLocationChanged(Location loc) {
        MainActivity.coord[0] = loc.getLongitude();
        MainActivity.coord[1] = loc.getLatitude();
    }

    @Override
    public void onProviderDisabled(String provider) {}

    @Override
    public void onProviderEnabled(String provider) {}

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {}
}
